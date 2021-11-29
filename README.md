# Introduction

This is an E-Commerce website specifically for dairy products. We are planning to build the following features.

1. User Authentication and Registration
2. Portal to list different products
3. Functionality to select products
4. Functionality to select mode of delievery
5. ...

## Tech Stack

- Django
- Python
- HTML, CSS, Bootstrap
- JS, JQuery

## Group Members

| Name            | Roll no |
| --------------  | ------- |
| Rochak Pandey   | 49      |
| Rohit Sharma    | 50      |


## DB Design

### MODELS

All models will inherit from the BASE model.

Common Properties:
- ID : UUID
- Created At : DateTime

1. Item
    1. Name
    2. Description
    3. Image Id - (F.K.) (Many to One)
    4. Order - (F.K.) (Many to Many)
    5. Price
    6. Discount
    7. Category - (F.K.) (Many to Many)

2. Orders
    1. Discount
    2. Payment Id - (F.K.) (One to One)
    3. Mode of Delievery [Home Delievery, Pickup]
    4. Address
    5. Customer (F.K.) (Many to One)

3. Image
    1. Alternate Text
    2. Image Url

4. Customer
    1. Name
    2. Email
    3. Password
    4. Last Login At
    5. Address (F.K.) (One to Many)

5. Payments
    1. Amount
    2. Status: [Successful, Pending, Failed, Cancelled]

6. Category
    1. Name