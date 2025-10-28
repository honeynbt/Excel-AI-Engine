
# Generate synthetic unstructured data with 1000 rows and 5 columns
import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

num_rows = 1000

# Sample text templates for unstructured data
feedback_templates = [
    "The product quality is {adj1}. I would {rec} it to others.",
    "Customer service was {adj1}. The response time was {adj2}.",
    "Overall experience was {adj1}. The interface is {adj2} and {adj3}.",
    "I am {adj1} with the service. The team was {adj2}.",
    "The delivery was {adj1}. Product arrived in {adj2} condition.",
]

descriptions = [
    "Technical documentation for API integration",
    "User feedback on mobile application",
    "Product review and feature requests",
    "Customer complaint and resolution details",
    "Service quality assessment report",
]

adj_positive = ['excellent', 'great', 'outstanding', 'wonderful', 'fantastic', 'good', 'satisfactory', 'impressive']
adj_negative = ['poor', 'terrible', 'disappointing', 'unsatisfactory', 'bad', 'awful']
adj_neutral = ['okay', 'average', 'acceptable', 'decent', 'fair', 'reasonable']
recommendations = ['recommend', 'highly recommend', 'not recommend', 'maybe recommend']

def generate_feedback():
    template = random.choice(feedback_templates)
    sentiment = random.choice(['positive', 'negative', 'neutral'])
    
    if sentiment == 'positive':
        adj_pool = adj_positive
    elif sentiment == 'negative':
        adj_pool = adj_negative
    else:
        adj_pool = adj_neutral
    
    return template.format(
        adj1=random.choice(adj_pool),
        adj2=random.choice(adj_pool),
        adj3=random.choice(adj_pool),
        rec=random.choice(recommendations)
    )

def generate_long_text():
    sentences = [
        "This document contains important information about the system.",
        "The analysis reveals several key insights.",
        "Performance metrics indicate steady growth.",
        "User engagement has increased significantly.",
        "Technical specifications are detailed below.",
        "Implementation requires careful planning.",
        "Results exceed initial expectations.",
        "Further investigation is recommended.",
    ]
    return ' '.join(random.sample(sentences, random.randint(2, 5)))

# Create unstructured dataset
unstructured_data = {
    'record_id': range(1, num_rows + 1),
    'feedback': [generate_feedback() for _ in range(num_rows)],
    'description': [random.choice(descriptions) for _ in range(num_rows)],
    'comments': [generate_long_text() for _ in range(num_rows)],
    'notes': [f"Additional notes for record {i}: " + ' '.join(random.sample([
        'priority', 'urgent', 'review required', 'follow up needed', 'resolved', 
        'pending', 'in progress', 'completed'
    ], random.randint(1, 3))) for i in range(1, num_rows + 1)],
}

df_unstructured = pd.DataFrame(unstructured_data)

print("Unstructured Data Sample:")
print(df_unstructured.head(10))
print(f"\nShape: {df_unstructured.shape}")
print(f"Data types:\n{df_unstructured.dtypes}")

# Show sample text content
print("\nSample Feedback:")
for i in range(5):
    print(f"{i+1}. {df_unstructured['feedback'].iloc[i]}")

# Save to CSV
df_unstructured.to_csv('unstructured_data.csv', index=False)
print("\n✓ Unstructured data saved to unstructured_data.csv")
