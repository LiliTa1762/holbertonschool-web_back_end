#!/usr/bin/env python3

from typing import Tuple, Dict, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    return ((page - 1) * page_size), page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page and number of item taking into account the page_size
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start_index, end_index = index_range(page, page_size)
        list_dataset = []
        list_dataset = self.dataset()
        if start_index > len(self.dataset()):
            return []
        return list_dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        data_value = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = 0
        if page + 1 < total_pages:
            next_page = page + 1
        else:
            next_page = None

        prev_page = 0
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': data_value,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
