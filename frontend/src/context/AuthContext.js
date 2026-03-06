import React, { createContext, useState, useContext, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext(null);

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Configure axios defaults with credentials for cookies
  axios.defaults.baseURL = API_URL;
  axios.defaults.withCredentials = true; // Enable sending cookies

  // Verify authentication on mount
  useEffect(() => {
    verifyAuth();
  }, []);

  const verifyAuth = async () => {
    try {
      const response = await axios.get('/api/auth/verify');
      setUser(response.data.user);
      setLoading(false);
    } catch (err) {
      setUser(null);
      setLoading(false);
    }
  };

  const login = async (email, password) => {
    try {
      setError(null);
      const response = await axios.post('/api/auth/login', {
        email,
        password
      }, {
        withCredentials: true
      });
      
      // Cookies are set automatically by the server
      setUser(response.data.user);
      return { success: true };
    } catch (err) {
      const errorMessage = err.response?.data?.message || 'Login failed. Please try again.';
      setError(errorMessage);
      return { success: false, error: errorMessage };
    }
  };

  const register = async (name, email, password) => {
    try {
      setError(null);
      const response = await axios.post('/api/auth/register', {
        name,
        email,
        password
      }, {
        withCredentials: true
      });
      
      // Cookies are set automatically by the server
      setUser(response.data.user);
      return { success: true };
    } catch (err) {
      const errorMessage = err.response?.data?.message || 'Registration failed. Please try again.';
      setError(errorMessage);
      return { success: false, error: errorMessage };
    }
  };

  const logout = async () => {
    try {
      await axios.post('/api/auth/logout', {}, { withCredentials: true });
    } catch (err) {
      // Continue with logout even if request fails
      console.error('Logout request failed:', err);
    } finally {
      setUser(null);
    }
  };

  const value = {
    user,
    loading,
    error,
    login,
    register,
    logout,
    isAuthenticated: !!user
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
