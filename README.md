# FastApi-order
## 題目一
### 問題一：
```sql
SELECT bnbs.id AS bnb_id, 
       bnbs.name AS bnb_name, 
       SUM(orders.amount) AS may_amount
FROM orders
JOIN bnbs ON orders.bnb_id = bnbs.id
WHERE orders.currency = 'TWD'
  AND orders.created_at >= '2023-05-01'
  AND orders.created_at < '2023-06-01'
GROUP BY bnbs.id, bnbs.name
ORDER BY may_amount DESC
LIMIT 10;
```
### 問題二：
建立索引 (Indexing):

確認在 orders 表的 currency、 created_at 欄位上建立索引，以加快查詢條件的過濾速度以及日期的查詢，在 orders 和 bnbs 表的 bnb_id 欄位上建立索引，以加快 JOIN 操作。
```sql
CREATE INDEX idx_orders_currency ON orders (currency);
CREATE INDEX idx_orders_created_at ON orders (created_at);
CREATE INDEX idx_orders_bnb_id ON orders (bnb_id);
CREATE INDEX idx_bnbs_id ON bnbs (id);
```
## 題目二
### 運行方式
建立、運行容器
```bash
docker-compose build
docker-compose up
```
Port 為 8080

## 使用的 SOLID 原則與設計模式

### SOLID 原則

#### 單一職責原則（SRP）
每個類只有一個職責。`OrderValidatorImpl` 類只負責驗證訂單的有效性，而 `OrderConverterImpl` 類只負責訂單的貨幣轉換。

#### 開放封閉原則（OCP）
通過抽象類 `OrderValidator` 和 `OrderConverter`，系統可以通過擴展來增加新功能，而無需修改現有程式。

#### 里氏替換原則（LSP）
`OrderValidatorImpl` 和 `OrderConverterImpl` 可以替代其基類 `OrderValidator` 和 `OrderConverter`，確保程序的正確性。

#### 介面隔離原則（ISP）
將驗證和轉換的介面分離成 `OrderValidator` 和 `OrderConverter`，客戶端可以根據需要選擇實現特定介面。

#### 依賴反轉原則（DIP）
高模組依賴於抽象介面 `OrderValidator` 和 `OrderConverter`，而不是具體實現。

### 設計模式

#### 工廠模式（Factory Pattern）
使用 `get_order_validator` 和 `get_order_converter` 工廠方法創建對象實例，而不是直接在代碼中實例化對象。

#### 依賴注入模式（Dependency Injection Pattern）
通過依賴注入模式，在 FastAPI 處理函數中獲取 `OrderValidator` 和 `OrderConverter` 的實例，解耦對象的創建和使用。

