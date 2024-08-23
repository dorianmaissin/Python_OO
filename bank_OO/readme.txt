Code structure:
- Create a bank class
    - name
    - address
    - user
    method:
        - get interest
        - send prime of 0.50 if a saving account is open
    -
- Create a user class
    - first name
    - last name
    - age
    - email
    - bank
    - birthday
    - accounts numbers
    methods :
        - create openning account
        - cash out some money
        - display account
- Create a account class
    - first name
    - last name
    - type
    - account number
    - amount
    - owner
    - opening date
    - interest
    methods: 
        - send money between own account
        - send money to external account
        - delete an accout
        - deposite money on the account

The account class will have two instance: current, saving

the user class will be the parent of the account class

the bank class will be the parent of the user clas