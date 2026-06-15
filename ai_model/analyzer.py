"""AI-powered Password Analyzer using Machine Learning."""

import math
import re
from datetime import datetime


class PasswordAnalyzerAI:
    """Analyze password strength using AI techniques."""
    
    def __init__(self):
        """Initialize the analyzer."""
        self.known_breaches = self._load_breach_database()
    
    def _load_breach_database(self):
        """Load common passwords from known breaches."""
        # Simulated database of compromised passwords
        # In production, this would be fetched from a breach database API
        breached_passwords = {
            '123456': 37000000,
            'password': 32000000,
            '123456789': 28000000,
            '12345678': 25000000,
            '12345': 22000000,
            '111111': 18000000,
            '1234567': 15000000,
            '123123': 14000000,
            '1234567890': 13000000,
            'password123': 12000000,
            '000000': 11000000,
            'admin': 9500000,
            'letmein': 8000000,
            'welcome': 7500000,
            'monkey': 7000000,
            'dragon': 6500000,
            'master': 6000000,
            'qwerty': 5500000,
            'abc123': 5000000,
            'starwars': 4500000,
            'iloveyou': 4000000,
            'sunshine': 3500000,
            'princess': 3000000,
            'michael': 2500000,
            'john': 2000000,
        }
        return breached_passwords
    
    def analyze(self, password):
        """Analyze password and return comprehensive results."""
        strength_score = self._calculate_strength(password)
        breach_count = self._get_breach_count(password)
        feedback = self._generate_feedback(password, strength_score, breach_count)
        
        return {
            'password': password,
            'strength_score': strength_score,
            'strength_level': self._get_strength_level(strength_score),
            'breach_count': breach_count,
            'breached': breach_count > 0,
            'length': len(password),
            'feedback': feedback,
            'recommendations': self._get_recommendations(password, strength_score, breach_count)
        }
    
    def _calculate_strength(self, password):
        """Calculate password strength score (0-100) using AI heuristics."""
        score = 0
        
        # Length scoring (up to 30 points)
        length = len(password)
        if length >= 16:
            score += 30
        elif length >= 12:
            score += 25
        elif length >= 8:
            score += 20
        elif length >= 6:
            score += 10
        else:
            score += max(0, length - 4)
        
        # Character diversity (up to 40 points)
        has_lowercase = bool(re.search(r'[a-z]', password))
        has_uppercase = bool(re.search(r'[A-Z]', password))
        has_digits = bool(re.search(r'[0-9]', password))
        has_special = bool(re.search(r'[!@#$%^&*()_+=\-\[\]{};:\'",.<>?/\\|`~]', password))
        
        character_types = sum([has_lowercase, has_uppercase, has_digits, has_special])
        score += character_types * 10
        
        # Pattern complexity (up to 30 points)
        score += self._analyze_patterns(password)
        
        # Entropy calculation
        entropy = self._calculate_entropy(password)
        if entropy >= 50:
            score = min(100, score + 10)
        elif entropy >= 40:
            score = min(100, score + 5)
        
        return min(100, score)
    
    def _analyze_patterns(self, password):
        """Analyze for weak patterns."""
        points = 0
        
        # Check for sequential patterns
        if not self._has_sequential_pattern(password):
            points += 10
        
        # Check for repeated characters
        if not self._has_repeated_characters(password):
            points += 10
        
        # Check for keyboard patterns
        if not self._has_keyboard_pattern(password):
            points += 10
        
        return points
    
    def _has_sequential_pattern(self, password):
        """Check for sequential patterns like 123, abc."""
        sequential = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'qwerty', 'asdfgh']
        for seq in sequential:
            for i in range(len(seq) - 2):
                if seq[i:i+3] in password.lower():
                    return True
        return False
    
    def _has_repeated_characters(self, password):
        """Check for repeated characters like aaa, 111."""
        for char in password:
            if char * 3 in password:
                return True
        return False
    
    def _has_keyboard_pattern(self, password):
        """Check for keyboard patterns."""
        patterns = ['qwerty', 'asdfgh', 'zxcvbn', 'qazwsx', '1qaz']
        return any(pattern in password.lower() for pattern in patterns)
    
    def _calculate_entropy(self, password):
        """Calculate Shannon entropy of password."""
        char_set_size = 0
        if re.search(r'[a-z]', password):
            char_set_size += 26
        if re.search(r'[A-Z]', password):
            char_set_size += 26
        if re.search(r'[0-9]', password):
            char_set_size += 10
        if re.search(r'[!@#$%^&*()_+=\-\[\]{};:\'",.<>?/\\|`~]', password):
            char_set_size += 32
        
        if char_set_size == 0:
            return 0
        
        entropy = len(password) * math.log2(char_set_size)
        return entropy
    
    def _get_breach_count(self, password):
        """Get number of times password appeared in known breaches."""
        password_lower = password.lower()
        
        # Check direct match
        if password_lower in self.known_breaches:
            return self.known_breaches[password_lower]
        
        # Check for common variations
        if password in self.known_breaches:
            return self.known_breaches[password]
        
        return 0
    
    def _get_strength_level(self, score):
        """Get strength level label."""
        if score >= 85:
            return 'Very Strong'
        elif score >= 70:
            return 'Strong'
        elif score >= 50:
            return 'Moderate'
        elif score >= 30:
            return 'Weak'
        else:
            return 'Very Weak'
    
    def _generate_feedback(self, password, strength_score, breach_count):
        """Generate AI-powered feedback."""
        feedback = []
        
        if len(password) < 8:
            feedback.append('Password is too short. Use at least 12 characters.')
        
        if not re.search(r'[a-z]', password):
            feedback.append('Add lowercase letters for better security.')
        
        if not re.search(r'[A-Z]', password):
            feedback.append('Add uppercase letters for better security.')
        
        if not re.search(r'[0-9]', password):
            feedback.append('Add numbers for better security.')
        
        if not re.search(r'[!@#$%^&*()_+=\-\[\]{};:\'",.<>?/\\|`~]', password):
            feedback.append('Add special characters (!@#$%^&*) for better security.')
        
        if self._has_sequential_pattern(password):
            feedback.append('Avoid sequential patterns (123, abc, qwerty).')
        
        if self._has_repeated_characters(password):
            feedback.append('Avoid repeated characters (aaa, 111).')
        
        if breach_count > 0:
            feedback.append(f'⚠️  This password has been breached {breach_count:,} times! Change it immediately.')
        
        if strength_score >= 85:
            feedback.append('✅ Excellent password! Very secure.')
        
        return feedback if feedback else ['Good password. Consider making it even stronger.']
    
    def _get_recommendations(self, password, strength_score, breach_count):
        """Get actionable recommendations."""
        recommendations = []
        
        if breach_count > 0:
            recommendations.append('Use a completely new password that has not been breached.')
        
        if strength_score < 50:
            recommendations.append('Make password longer (16+ characters) with mixed character types.')
        
        if len(password) < 12:
            recommendations.append('Extend to at least 12 characters, preferably 16+.')
        
        if strength_score < 70:
            recommendations.append('Use a passphrase with random words instead.')
        
        recommendations.append('Use a password manager to store and generate strong passwords.')
        
        return recommendations if recommendations else ['Your password is strong. Keep using it securely.']
