# Floyd Recursive

This repository contains an implementation of Floyd's algorithm in a recursive manner. Floyd's algorithm, also known as the Floyd-Warshall algorithm, is used to find the shortest paths between all pairs of vertices in a weighted graph.

## To start, make sure to:

1. Install all requirements located in the `requirements.txt` file, using the pip command `pip install -r requirements.txt`.
2. Clone the repository to your own machine in a certain location.
3. Using the terminal, use the "cd" function to locate a directory, see this example, `CD C:\Users\mrqad\Documents\GitHub\floyd-recursion\src`. Make sure you choose the `src` file.
4. Once your local directory is identified, run the code ```python recursive_floyd.py```

You should see a similar output ```[[0, 7, 12, 8], [9223372036854775807, 0, 5, 7], [9223372036854775807, 9223372036854775807, 0, 2], [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]```

## Testing

You may find the testing script inside the testing folder in the repository. The tests were ran individually.

## Performance Comparison 

You may find a code that compares the performance between the recursive and imperative application methods of this algorithm. This is located in the testing folder.

## Contributing

Given my developing knowledge of this field, feedback and contributions to this project are welcome! If you find any issues or have suggestions for improvements, please feel free to contact me.

## License

This project is licensed under the Apache 2.o license.
Feel free to use and modify the code according to the terms of the license.

## Directory Tree
``` floyd-recursion

├── src

│   ├── imperative_floyd.py

│   └── recursive_floyd.py

├── testing

│   ├── imperative_floyd.py

│   ├── performance_comparison.py

│   ├── recursive_floyd.py

│   └── testing_floyd.py

├── license.txt

├── readme.md

├── requirements.txt

└── setup.py
```
