# Scratch Bling API, but it's Python

This is a simple API developed as an assessment for Byte.lion

## Documentation

### API Endpoints

| API endpoint | HTTP method | Description                                                                                |
| ------------ | ----------- | ------------------------------------------------------------------------------------------ |
| /items       | GET         | Retrieves a list of all items                                                              |
| /items/[id]  | GET         | Retrieves an item by its ID (ex: /items/1)                                                 |
| /items       | POST        | Creates an item using the request body format below                                        |
| /items/[id]  | DELETE      | Deletes an item by its ID, must be URL encoded (ex: /items/1)                              |
| /items/[id]  | PUT         | Edits an item by its ID, must be URL encoded **and** include a request body (format below) |

### Request Body

For POST and PUT requests, use a `x-www-form-urlencoded` body with the following fields:

| Field name                  | Data type |
| --------------------------- | --------- |
| item_name (required)        | String    |
| item_description (required) | String    |
| item_size (required)        | Array     |
| item_cost (required)        | String    |
