
> It is a draft

> Interesting example of code is located in `api_gateway/main.py`. 
> The endpoint emulates gathering the different data from the several external sources (e.g. these might be a standalone microservices with rest API).

# todo_fastapi
A little learning project built with FastAPI framework.

# Description
For learning purposes, the app is split into standalone services:
- users
- tasks

The code of every service is segregated to the layers:
- presentation
- business logic
- data access

### Presentation layer
This includes rest API endpoints, events handlers and communication with external (including other todo's services) services.
The code of the presentation layer just: 
- validates data
- restructures to propagate needed parts to the business logic services
- aggregates data gotten from the business logic layer and external services

### Business logic layer
This does everything that reflects the features from UX experience excluding the low-level technical implementation.

### Data access layer
Just CRUD. Any sort of storages. The structure of data in the storage could radically differ from business entities.


# Just raw notes

Tasks
History
Reminders
Tags
Projects
Reminders
Configuration
  --- hide done / cross out
Free/Premium
Comments
Filters (including saved presets)

# 1st Release
Tasks list with all fields
Reminders as fake.

## [Tasks Service]
### Task Domain Model:
- title
- description
- deadline_at - the final datetime when the task must be completed
- scheduled_at - the date when the assignee wants to do something related to the task

## [Reminders Service]
### Reminder Domain Model:
- task_id
- schedule: Schedule Model
- next_sending_at - datetime where a letter/push notification should be sent

### Schedule Domain Model:
_There are several different types of the model based on type_
### DeltaSchedule Domain Model:
- value
- time_unit: days/hours/minutes/seconds
### DatetimeSchedule:
- datetime (with timezone)

### Task Event Handler:
_When task is created/updated then the event is published and 
this service updates all reminders 
???(perhaps api-gateway in POST/PATCH request should let "reminders service" know the needed data 
regarding task and reminding)???_
- 

## Celery tasks:
### Send reminders:
  - get reminders with datetime (`next_sending_at`) around now. Indexed field `next_sending_at`...
  - get task details (title, )

## [API Gateway Service]
### Get tasks Endpoint
Get tasks from Tasks Service.

### Get task detail endpoint
Get task properties.
Get reminders.

### Create task
Post properties to Tasks Service
Post reminders properties to Reminders Service.
If both internal requests are successful then client's response is 201.
_Rollback in other services if some internal request is failed_
_A model DistributionTransaction and FK in all other models can be used_ 
