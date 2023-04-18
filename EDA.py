#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Load the dataset
yahoo_stock = pd.read_csv("NEWS_YAHOO_stock_prediction.csv")


# In[3]:


# Preview the dataset
yahoo_stock.head()


# In[4]:


# Create correlation matrix of numerical variables
num_vars = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
corr_mat = yahoo_stock[num_vars].corr()


# In[5]:


# Create heatmap of correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(corr_mat, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix Heatmap")
plt.show()


# In[7]:


# Boxplot of stock price by ticker
plt.figure(figsize=(8, 6))
sns.boxplot(x='ticker', y='Open', data=yahoo_stock, palette='coolwarm')
plt.title("Boxplot of Opening Stock Prices by Ticker")
plt.xlabel("Ticker")
plt.ylabel("Opening Stock Price")
plt.show()


# In[8]:


plt.figure(figsize=(8, 6))
sns.boxplot(x='ticker', y='Close', data=yahoo_stock, palette='coolwarm')
plt.title("Boxplot of Closing Stock Prices by Ticker")
plt.xlabel("Ticker")
plt.ylabel("Closing Stock Price")
plt.show()


# In[9]:


# Line plot of stock price by ticker over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Open', hue='ticker', data=yahoo_stock)
plt.title("Opening Stock Prices by Ticker over Time")
plt.xlabel("Date")
plt.ylabel("Opening Stock Price")
plt.xticks(rotation=45)
plt.show()


# In[10]:


plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Close', hue='ticker', data=yahoo_stock)
plt.title("Closing Stock Prices by Ticker over Time")
plt.xlabel("Date")
plt.ylabel("Closing Stock Price")
plt.xticks(rotation=45)
plt.show()


# In[11]:



# Descriptive statistics of numerical variables
yahoo_stock.describe()


# In[12]:


# Distribution plot of opening and closing stock prices
plt.figure(figsize=(10, 6))
sns.histplot(data=yahoo_stock, x='Open', hue='ticker', kde=True)
plt.title("Distribution of Opening Stock Prices by Ticker")
plt.xlabel("Opening Stock Price")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=yahoo_stock, x='Close', hue='ticker', kde=True)
plt.title("Distribution of Closing Stock Prices by Ticker")
plt.xlabel("Closing Stock Price")
plt.show()


# In[15]:


# Scatter plot of opening and closing stock prices
plt.figure(figsize=(8, 6))
sns.scatterplot(data=yahoo_stock, x='Open', y='Close', hue='ticker', palette='coolwarm')
plt.title("Scatter Plot of Opening and Closing Stock Prices")
plt.xlabel("Opening Stock Price")
plt.ylabel("Closing Stock Price")
plt.show()


# In[ ]:




