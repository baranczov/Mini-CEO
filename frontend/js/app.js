document.getElementById('offerForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        income: parseInt(document.getElementById('income').value),
        is_loyal: document.getElementById('is_loyal').checked,
        churn_score: parseFloat(document.getElementById('churn_score').value),
        gas_avg_check: parseInt(document.getElementById('gas_avg_check').value),
        has_debit_card: document.getElementById('has_debit_card').checked,
        has_credit_card: document.getElementById('has_credit_card').checked
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });

        const data = await response.json();
        const resultDiv = document.getElementById('result');
        const text = document.getElementById('recommendationText');

        resultDiv.style.display = 'block';

        if (data.offer_found) {
            text.innerHTML = `
                <strong>Продукт:</strong> ${data.product_name}<br>
                <strong>Канал:</strong> ${data.channel}<br>
                <strong>Ожидаемая ценность (EV):</strong> ${data.expected_value} ₽
            `;
            resultDiv.style.backgroundColor = '#65b891'; // Цвет успеха
        } else {
            text.innerText = "Клиенту не рекомендуется делать предложение (низкий Uplift или риск оттока).";
            resultDiv.style.backgroundColor = '#4e878c';
        }
    } catch (error) {
        alert("Ошибка связи с сервером. Проверьте, запущен ли FastAPI.");
    }
});