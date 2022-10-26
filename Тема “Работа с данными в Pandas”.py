import pandas as pd

# Задание 1

authors = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']}, columns=['author_id', 'author_name']

                       )

book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                     'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой',
                                    'Гроза', 'Таланты и поклонники'],
                     'price': [450, 300, 350, 500, 450, 370, 290]}, columns=['author_id', 'book_title', 'price']
                    )

# Задание 2

authors_price = authors.merge(book)

# Задание 3

top5 = authors_price.sort_values(by=['price'], ascending=False).head()

# Задание 4

name_list = []
max_price_list = []
min_price_list = []
mean_list = []
for i in range(1, 4):
    name_list.append(authors_price.loc[authors_price['author_id'] == i, 'author_name'].iloc[0])
    max_price_list.append(authors_price.loc[authors_price['author_id'] == i, "price"].max())
    min_price_list.append(authors_price.loc[authors_price['author_id'] == i, "price"].min())
    mean_list.append(authors_price.loc[authors_price['author_id'] == i].describe().loc['mean', 'price'])
    mean = authors_price.loc[authors_price['author_id'] == i].describe().loc['mean', 'price']

authors_stat = pd.DataFrame({"author_name": name_list,
                             "min_price": max_price_list,
                             "max_price": min_price_list,
                             "mean_price": mean_list}, columns=["author_name", "min_price", "max_price", "mean_price"])
