import logging
from threading import Thread, Event
from queue import Empty
from multiprocessing import Queue
from collections import defaultdict

log = logging.getLogger(__name__)

class QueueProcessor(Thread):

	def __init__(self, data_q, log_level=None, *args, **kwargs):
		super(QueueProcessor, self).__init__(*args, **kwargs)
		self.q = data_q
		self._response_handlers = {'unsubscribed':self._handler_unsubscribed,
		'subscribed':self._handle_subscribed,
		'conf':self._handle_auth,
		'unauth':self._handle_auth}

		self._data_handlers = {'ticker':self._handle_ticker,
		'book':self._handle_book,
		'raw_book':self._handle_raw_book,
		'candles':self._handle_candles,
		'trades':self._handle_trades}

		self._register = {}
		self.channel_directory = {}
		self.channel_handlers = {}

		self.last_update = {}
		self.tickers = defaultdict(Queue)
		self.books = defaultdict(Queue)
		self.raw_books = defaultdict(Queue)
		self.trades = defaultdict(Queue)
		self.candles = defaultdict(Queue)
		self.account = Queue()

		self._stopped = Event()
		self.log = logging.getLogger(self.__module__)
		self.log.setLevel(level=logging.INFO if not log_level else log_level)