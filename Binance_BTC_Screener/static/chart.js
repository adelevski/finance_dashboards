var chart = LightweightCharts.createChart(document.getElementById('chart'), {
	width: 1000,
  	height: 500,
	layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	priceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
		timeVisible: true,
		secondsVisible: false,
	},
});

var candleSeries = chart.addCandlestickSeries({
  upColor: 'rgba(0, 255, 0, 1)',
  downColor: 'rgba(255, 0, 0, 1)',
  borderDownColor: 'rgba(255, 0, 0, 1)',
  borderUpColor: 'rgba(0, 255, 0, 1)',
  wickDownColor: 'rgba(255, 0, 0, 1)',
  wickUpColor: 'rgba(0, 255, 0, 1)',
});


fetch('http://localhost:5000/history')
	.then((r) => r.json())
	.then((response) => {
		console.log(response);

		candleSeries.setData(response);
	})


var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_1m");

binanceSocket.onmessage = function (event) {	
		
	var message = JSON.parse(event.data);

	var candlestick = message.k;

	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c
	})
}