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
