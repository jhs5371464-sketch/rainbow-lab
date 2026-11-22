import json, pathlib, datetime, time
import yfinance as yf

ROOT=pathlib.Path(__file__).parent
TICKERS=['SOXX','QQQ','SPY','TQQQ','SMH','NVDA','VOO','BTC-USD','QLD','SOXL','SCHD','JEPQ','AAPL','MSFT','META','TSLA','AMD','AVGO','GOOGL','AMZN']
failed=[]
for ticker in TICKERS:
    try:
        df=yf.Ticker(ticker).history(period='max', interval='1wk', auto_adjust=True)
        if df.empty or len(df)<20: raise ValueError('insufficient history')
        points=[[str(idx.date()),round(float(row['Close']),6)] for idx,row in df.iterrows() if float(row['Close'])>0]
        payload={'ticker':ticker,'updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'price_type':'adjusted weekly close','source':'Yahoo Finance via yfinance','data':points}
        path=ROOT/'data'/f'{ticker}.json';path.write_text(json.dumps(payload,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
        print(ticker,len(points))
    except Exception as exc:
        failed.append(ticker);print('FAILED',ticker,exc)
    time.sleep(1)
if failed: print('Failed tickers:',', '.join(failed))
if len(failed)==len(TICKERS): raise SystemExit('All updates failed')
