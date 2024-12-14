### Required libraries
pip install mimesis=18.0.0

### Name of the sqlite file to add data to
sqlfile=test.db

### Number of person records to create, can be omitted
person=10

### Number of payment records to create, can be omitted
payment=10

### Number of food records to create, can be omitted
food=10

### Number of address records to create, can be omitted
address=10

### Number of finance records to create, can be omitted
finance=10

### The value to use as the random seed
#### keep this the same for predictive results
#### omit and get random values
global_seed="fund"

### Example command line: 
python main.py sqlfile=test1.db person=10 payment=10 food=10 address=10 finance=10 global_seed="fund"
