import aio_pika
import aio_pika.abc
import asyncio


@app.get("/sandbox/publish-event")
async def rab():
    loop = asyncio.get_event_loop()
    await publish_event(loop)
    return {"result": "ok"}


async def publish_event(loop):
    # Explicit type annotation
    connection: aio_pika.RobustConnection = await aio_pika.connect_robust(
        "amqp://rabbit:rab@rabbit/", loop=loop
    )
    print("========== connection")
    print(connection)
    print("==========")
    async with connection:
        queue_name = "test_queue"
        routing_key = "test_queue"
        print("----- 1")

        # Creating channel
        channel: aio_pika.abc.AbstractChannel = await connection.channel()
        print("----- 2")

        # Declaring queue
        queue = await channel.declare_queue(queue_name, auto_delete=True)
        print("----- 3")

        print("----- 4 out of 'with'")

        # Declaring exchange
        exchange = await channel.declare_exchange("direct", auto_delete=True)
        # Binding queue
        await queue.bind(exchange, routing_key)

        await channel.default_exchange.publish(
            aio_pika.Message(body="Hello {}".format(routing_key).encode()),
            routing_key=routing_key,
        )

        # Receiving message
        incoming_message = await queue.get(timeout=5)
        print("##################### incoming_message")
        print(incoming_message)
        print("######## body")
        print(incoming_message.body)
        print("########")

        # Confirm message
        await incoming_message.ack()
        await queue.unbind(exchange, routing_key)

    # await connection.close()
