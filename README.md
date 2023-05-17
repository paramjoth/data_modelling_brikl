# data_modelling_brikl
Algorithm Problem
Coin Exchange
Let’s build a program that will be used in the Coin Exchange Center to input the
coins they have and the amount of given money that can be exchanged into coins
with the least number of coins possible returned from the largest coin down to the
smallest coin.
For example, A Central branch only has [1, 5, 7, 9, 11] coins, and then your
customer comes in with the 25 amount of money.
The program should return 3, from 11 + 9 + 5.
Sometimes, our coins left in any branch may need to be made available or sufficient
for exchange.
For example, if the sub-branch only has [7, 9] coins, a customer wants to exchange
for 20.
The program should return -1
Test Inputs

Supplier Integration, Backend 2

Case 1
Coins: [1, 5, 7, 9, 11]
Input: 25
Output: 3 ( 11 + 9 + 5 )
Case 2
Coins: [1, 5, 7, 9, 11]
Input: 14
Output: 2 (9 + 5)
Case 3
Coins: [7, 9]
Input: 20
Output -1 (insufficient coins available for exchange)

Data Modeling
Delivery: Python classes
Requirement:
On our Brikl platform, users can create a new Storefront or MicroStore as much
as they like.
For MicroStore, users are allowed to display only their promotional products*,
which contain many products inside.
But for the Storefront, users are allowed to display any products that they have
in their inventory.
A product can have multiple attributes to describe what a product could look like,
which consist of a title, description, price, available date, stock quantity, and
product images.
Also, for the store product listing page, customers allowing to search and filter
for a specific product depending on criteria such as the product’s category,
newest/oldest, or availability status (in-stock or out-of-stock)

Supplier Integration, Backend 3

* customized products from the based product for specific
stores/businesses/brands this could be a shirt/mug with the logo of the brand

Database
Delivery: SQL table schemas
Please help design your SQL table schemas from the requirement and Python
models above.
