這是我的倉位大小計算機的前端代碼：

```html
<!DOCTYPE html>
<html lang="UTF-8">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/css/index.css">
    <script src="../static/script/index.js"></script>
</head>
<body class="wrap">
    <div class="form">
        <div class="title">仓位大小计算机</div>
        <div class="subtitle">Designed by BTCLION</div>
        <div class="input-container ic1">
            <input id="total-funds" class="input" type="text" placeholder=" " />
            <div class="cut"></div>
            <label for="total-funds" class="placeholder">请输入您的总资金（USDT）</label>
        </div>
        <div class="input-container ic2">
            <input id="accept-loss" class="input" type="text" placeholder=" " />
            <div class="cut cut-long"></div>
            <label for="accept-loss" class="placeholder">可接受止损百分比（建议低於5%）</label>
        </div>
        <div class="input-container ic2">
            <input id="strategy-loss" class="input" type="text" placeholder=" " />
            <div class="cut cut-short"></div>
            <label for="strategy-loss" class="placeholder">策略止损百分比</>
        </div>
        <button type="text" class="calculate">计算</button>
        <div class="result-message"></div>
      </div>
</body>
</html>
```

```css
body {
    align-items: center;
    background-color: #000;
    display: flex;
    justify-content: center;
    height: 100vh;
}
  
.form {
    background-color: #15172b;
    border-radius: 20px;
    box-sizing: border-box;
    height: auto;
    padding: 20px;
    width: 320px;
    opacity: 0;
    transition: opacity 1s ease;
}

.form.fadeIn {
    opacity: 1;
}
  
.title {
    color: #eee;
    font-family: sans-serif;
    font-size: 32px;
    font-weight: 600;
    margin-top: 30px;
    text-align: center;
}
  
.subtitle {
    color: #eee;
    font-family: sans-serif;
    font-size: 16px;
    font-weight: 600;
    margin-top: 10px;
    text-align: center;
}
  
.input-container {
    height: 50px;
    position: relative;
    width: 100%;
}
  
.ic1 {
    margin-top: 40px;
}
  
.ic2 {
    margin-top: 30px;
}
  
.input {
    background-color: #303245;
    border-radius: 12px;
    border: 0;
    box-sizing: border-box;
    color: #eee;
    font-size: 18px;
    height: 100%;
    outline: 0;
    padding: 4px 20px 0;
    width: 100%;
}
  
.cut {
    background-color: #15172b;
    border-radius: 10px;
    height: 20px;
    left: 20px;
    position: absolute;
    top: -20px;
    transform: translateY(0);
    transition: transform 400ms;
    width: 164px;
}
  
.cut-long {
    width: 153px;
}
.cut-short {
    width: 103px;
}
  
.input:focus ~ .cut,
.input:not(:placeholder-shown) ~ .cut {
    transform: translateY(8px);
}
  
.placeholder {
    color: #65657b;
    font-family: sans-serif;
    left: 20px;
    line-height: 14px;
    pointer-events: none;
    position: absolute;
    transform-origin: 0 50%;
    transition: transform 400ms, color 400ms;
    top: 20px;
}
  
.input:focus ~ .placeholder,
.input:not(:placeholder-shown) ~ .placeholder {
    transform: translateY(-30px) translateX(10px) scale(0.75);
}
  
.input:not(:placeholder-shown) ~ .placeholder {
    color: #808097;
}
  
.input:focus ~ .placeholder {
    color: #65657b;
}
  
.calculate {
    background-color: #08d;
    border-radius: 12px;
    border: 0;
    box-sizing: border-box;
    color: #eee;
    cursor: pointer;
    font-size: 18px;
    height: 50px;
    margin-top: 38px;
    outline: 0;
    text-align: center;
    width: 100%;
}
  
.calculate:active {
    background-color: #06b;
}


.result-message {
    opacity: 0;
    max-height: 0;
    overflow: hidden;
    margin-top: 30px;
    margin-bottom: 10px;
    color: #eee;
    font-size: 18px;
    font-family: sans-serif;
    text-align: center;
    transition: max-height 0.5s ease, opacity 0.5s ease;
}

.result-message.show {
    opacity: 1;
    max-height: 100px; /* 設置一個足夠大的值，以確保內容能夠完全展開 */
    transition: max-height 0.5s ease, opacity 0.5s ease;
}

```

```javascript
document.addEventListener('DOMContentLoaded', function () {
    // initialize
    const form = document.querySelector('.form');
    form.classList.add('fadeIn');
    const calculateButton = document.querySelector('.calculate');
    const totalFundsInput = document.getElementById('total-funds');
    const acceptLossInput = document.getElementById('accept-loss');
    const strategyLossInput = document.getElementById('strategy-loss');
    const resultMessageContainer = document.querySelector('.result-message');

    // calculate
    calculateButton.addEventListener('click', function () {
        // value setting
        const totalFunds = parseFloat(totalFundsInput.value);
        const acceptLoss = parseFloat(acceptLossInput.value);
        const strategyLoss = parseFloat(strategyLossInput.value);

        // stop loss warning
        if (acceptLoss/totalFunds > 0.05) {
            const userConfirmation = confirm(
                '警告：您的止损可能过高，有潜在的爆仓风险，仍要继续吗？'
            );
            if (!userConfirmation) {
                resultMessageContainer.textContent = '';
                return;
            }
        }

        // acceptable max position
        const maxPosition = acceptLoss / (strategyLoss / 100);

        // result
        const resultMessage = document.createElement('div');
        resultMessage.className = 'result-message';
        resultMessage.innerHTML = `您的可接受最大仓位（含杠杆）为<br>${maxPosition.toFixed(2)} USDT。`;
        resultMessage.classList.add('show');
        resultMessageContainer.innerHTML = '';
        resultMessageContainer.appendChild(resultMessage);
        resultMessageContainer.classList.add('show');
        form.style.height = 'auto';
    });
});

```