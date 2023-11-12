// 全域變數，儲存最後一次查詢結果
let lastQueryResult = {};

// 函數用於填充表格
function fillTable(table, data) {
  // 清空表格內容
  table.innerHTML = '';

  // 如果沒有資料，提供一個提示行
  if (data.length === 0) {
    const row = table.insertRow();
    const cell = row.insertCell(0);
    cell.colSpan = 5; // 設定合併的列數
    cell.textContent = 'No data available';
    return;
  }

  // 添加表頭
  const headerRow = table.insertRow();
  for (const key in data[0]) {
    const th = document.createElement('th');
    th.textContent = key;
    headerRow.appendChild(th);
  }

  // 添加資料行
  data.forEach(item => {
    const row = table.insertRow();
    for (const key in item) {
      const cell = row.insertCell();
      cell.textContent = item[key];
    }
  });
}

// 模擬從後端獲取的資料
const customers = [
  { customerId: '1', customerName: 'John Doe', address: '123 Main St', phoneNumber: '555-1234', emailAddress: 'john@example.com' },
  // 其他顧客資料...
];

const orders = [
  { orderId: 'A001', orderDate: '2023-01-01', customerId: '1', totalOrderPrice: 100.0, purchaseStatus: 'Paid' },
  // 其他訂單資料...
];

const products = [
  { productId: 'P001', productName: 'Product 1', categoryId: 'C001', productRemainQuantity: 50, productPrice: 19.99 },
  // 其他產品資料...
];

// 函數用於顯示查詢結果
function showQueryResult(queryType, result) {
  const infoDiv = document.getElementById(`${queryType}-info`);
  lastQueryResult = result; // 保存最後一次查詢結果
  fillTable(infoDiv, result);
}

// 函數用於查詢顧客
function searchCustomer() {
  const customerId = document.getElementById('customer-id-input').value;
  const result = customers.filter(customer => customer.customerId === customerId);
  showQueryResult('customer', result);
}

// 函數用於查詢訂單
function searchOrder() {
  const orderId = document.getElementById('order-id-input').value;
  const result = orders.filter(order => order.orderId === orderId);
  showQueryResult('order', result);
}

// 函數用於查詢產品
function searchProduct() {
  const productId = document.getElementById('product-id-input').value;
  const result = products.filter(product => product.productId === productId);
  showQueryResult('product', result);
}
