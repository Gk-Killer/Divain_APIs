import uvicorn
from fastapi import FastAPI, HTTPException
import psycopg2
from Divain.pgrs_dn_config import StockUpdate

app = FastAPI()

@app.get("/stocks")
def get_stocks():
    """
    Fetch stock data from the database.
    """
    try:
        stock_update = StockUpdate()
        records = stock_update.fetch_stock_data()
        if not records:
            raise HTTPException(status_code=404, detail="No stock data found")
        return {"stocks": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/stocks_movement")
def update_stock_movement(stock_id: str, mov_quantity: int, mov_type: str = 'in'):
    """
    Update stock movement in the database.
    """
    try:
        stock_update = StockUpdate()
        stock_update.update_stock_movement(stock_id, mov_quantity, mov_type)
        return {"message": "Stock movement updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stocks_movement_history")
def history_stock_mov():
    """
    Update stock quantity in the database.
    """
    try:
        stock_update = StockUpdate()
        records = stock_update.get_stock_movement_history()
        if not records:
            raise HTTPException(status_code=404, detail="No stock history found")
        return {"stocks History": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
   uvicorn.run(app, host="127.0.0.1", port=5003)
