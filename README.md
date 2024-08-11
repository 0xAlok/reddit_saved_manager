# Reddit Saved Posts Manager

This script processes a CSV file containing saved Reddit posts and groups them by subreddit. The output is saved to an Excel file.

## Prerequisites

- Python 3.x
- pandas library

You can install the required library using pip:

```sh
pip install pandas
```

## Steps to Use

1. Request Your Data from Reddit:
    - Go to [Reddit Data Request](https://www.reddit.com/settings/data-request) and request your data.
    - Once you receive your data, locate the CSV file containing your saved posts and saved comments. Ensure it has the columns id and permalink.

2. Prepare the Script:
    - Save the script as `subreddit_posts_processor.py`.
    - Use `subreddit_comments_processor.py` for saved comments.

3. Run the Script:
    - Place the CSV file in the same directory as the script or update the script with the correct path to your CSV file.
    - Open a terminal and navigate to the directory containing the script.
    - Run the script using Python.

```sh
python subreddit_posts_processor.py
```

4. Output:
    - The script will generate an Excel file named `saved_posts.xlsx` in the same directory, containing the grouped subreddit posts. `saved_comments` for comments.
  
## Script Details

The script performs the following steps:

1. Loads the CSV file containing the id and permalink columns.
2. Ensures there are no missing values in the permalink column.
3. Extracts the subreddit from each permalink and creates a new column for it.
4. Drops rows where subreddit extraction failed.
5. Groups the posts by subreddit.
6. Creates a new DataFrame with subreddits and their corresponding posts.
7. Saves the new DataFrame to an Excel file.

## Example

Here is an example of how the script processes the data:

-  Input csv file (`grouped_posts.csv`)
```sh
id,permalink
1,https://www.reddit.com/r/python/comments/abc123/example_post_1/
2,https://www.reddit.com/r/learnpython/comments/def456/example_post_2/
```

-  Output excel file (`saved_posts.xlsx`)
```sh
Subreddit       Posts
python          https://www.reddit.com/r/python/comments/abc123/example_post_1/
learnpython     https://www.reddit.com/r/learnpython/comments/def456/example_post_2/
```
## License

This project is licensed under the MIT License.
