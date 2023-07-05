# Matrix Application

A company produces three types of products: A, B, and C. The unit prices of the products are $10, $15, and $20 respectively. The company has two factories: X and Y. The production costs per unit for each product at each factory are given by the following matrix:

| Factory | Product A | Product B | Product C |
|---------|-----------|-----------|-----------|
| X       |     4     |     6     |     8     |
| Y       |     5     |     7     |    10     |

The rows represent the factories, and the columns represent the products. For example, the production cost of product A at factory X is $4.

The company wants to know how much profit it can make by selling the products from each factory. The sales figures for each product at each factory are given by the following matrix:

| Factory | Product A | Product B | Product C |
|---------|-----------|-----------|-----------|
| X       |    100    |    200    |    300    |
| Y       |    150    |    250    |    350    |

The rows represent the factories, and the columns represent the products. For example, the sales figure of product A from factory X is 100 units.

To find the profit matrix, we need to multiply the sales matrix by the unit price matrix and then subtract the production cost matrix. The unit price matrix is a diagonal matrix with the unit prices on the main diagonal:

|         | Product A | Product B | Product C |
|---------|-----------|-----------|-----------|
|Product A|    $10    |    $0     |    $0     |
|Product B|    $0     |    $15    |    $0     |
|Product C|    $0     |    $0     |    $20    |

Using matrix multiplication, we can find the profit matrix as follows:

| Factory | Product A                           | Product B                           | Product C                           |
|---------|-------------------------------------|-------------------------------------|-------------------------------------|
|    X    | (100x10)+(200x0)+(300x0) = 1000    | (100x0)+(200x15)+(300x0) = 3000    | (100x0)+(200x0)+(300x20) = 6000    |
|    Y    | (150x10)+(250x0)+(350x0) = 1500    | (150x0)+(250x15)+(350x0) = 3750    | (150x0)+(250x0)+(350x20) = 7000    |

The rows represent the factories, and the columns represent the products. For example, the profit from selling product A from factory X is $996.

To do this without matrix multiplication, we need to multiply each element of the sales matrix by the corresponding element of the unit price matrix and then subtract the corresponding element of the production cost matrix. For example, to find the profit from selling product A from factory X, we need to do:

(100 x 10) - 4 = 996

We can do this for every element of the matrices and get the same result as above. This method is more tedious and prone to errors than using matrix multiplication.￼Enter
