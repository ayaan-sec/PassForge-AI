// PassForge AI - Client-Side Application

document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('passwordInput');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const togglePasswordBtn = document.getElementById('togglePassword');
    const resultsDiv = document.getElementById('results');

    // Toggle password visibility
    if (togglePasswordBtn) {
        togglePasswordBtn.addEventListener('click', () => {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            togglePasswordBtn.textContent = type === 'password' ? '👁️' : '👁️‍🗨️';
        });
    }

    // Analyze password on button click
    if (analyzeBtn) {
        analyzeBtn.addEventListener('click', analyzePassword);
    }

    // Analyze password on Enter key
    if (passwordInput) {
        passwordInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                analyzePassword();
            }
        });
    }

    async function analyzePassword() {
        const password = passwordInput.value;

        if (!password) {
            alert('Please enter a password');
            return;
        }

        try {
            // Show loading state
            analyzeBtn.textContent = 'Analyzing...';
            analyzeBtn.disabled = true;

            // Call backend API
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ password: password }),
            });

            if (!response.ok) {
                throw new Error('Failed to analyze password');
            }

            const data = await response.json();

            // Display results
            displayResults(data);
        } catch (error) {
            console.error('Error:', error);
            alert('Error analyzing password. Please try again.');
        } finally {
            analyzeBtn.textContent = 'Analyze Password';
            analyzeBtn.disabled = false;
        }
    }

    function displayResults(data) {
        resultsDiv.classList.remove('hidden');

        // Update strength score
        const strengthScore = document.getElementById('strengthScore');
        const strengthLevel = document.getElementById('strengthLevel');
        const strengthBar = document.getElementById('strengthBar');

        strengthScore.textContent = `${data.strength_score}/100`;
        strengthLevel.textContent = data.strength_level;

        // Update strength bar color and width
        const strengthFill = strengthBar.querySelector('.strength-fill');
        strengthFill.className = 'strength-fill';

        const strengthClass = data.strength_level
            .toLowerCase()
            .replace(' ', '-');
        strengthFill.classList.add(strengthClass);

        // Update breach count
        const breachCount = document.getElementById('breachCount');
        const breachStatus = document.getElementById('breachStatus');

        breachCount.textContent = data.breach_count.toLocaleString();
        if (data.breached) {
            breachStatus.textContent = 'This password has been in data breaches!';
            breachStatus.classList.remove('safe');
        } else {
            breachStatus.textContent = 'This password has not been detected in known breaches.';
            breachStatus.classList.add('safe');
        }

        // Update feedback
        const feedbackList = document.getElementById('feedbackList');
        feedbackList.innerHTML = '';
        if (data.feedback && data.feedback.length > 0) {
            data.feedback.forEach((item) => {
                const li = document.createElement('li');
                li.textContent = item;
                feedbackList.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = 'No issues detected.';
            feedbackList.appendChild(li);
        }

        // Update recommendations
        const recommendationsList = document.getElementById('recommendationsList');
        recommendationsList.innerHTML = '';
        if (data.recommendations && data.recommendations.length > 0) {
            data.recommendations.forEach((item) => {
                const li = document.createElement('li');
                li.textContent = item;
                recommendationsList.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = 'Your password looks good!';
            recommendationsList.appendChild(li);
        }

        // Scroll to results
        setTimeout(() => {
            resultsDiv.scrollIntoView({ behavior: 'smooth' });
        }, 100);
    }
});
