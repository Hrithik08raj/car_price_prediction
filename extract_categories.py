import pickle
import json

with open('LinearRegressionModel.pkl', 'rb') as f:
    model = pickle.load(f)

# Try to find the OneHotEncoder in the pipeline
encoder = None
if hasattr(model, 'steps'):
    for name, step in model.steps:
        # Check if the step is a ColumnTransformer
        if hasattr(step, 'transformers_'):
            for t_name, t, cols in step.transformers_:
                if hasattr(t, 'categories_'):
                    encoder = t
                    break
        elif hasattr(step, 'categories_'):
            encoder = step
            break

if encoder is not None:
    categories = encoder.categories_
    # Often it's a list of arrays for each categorical feature
    # Let's just print the length and first 5 of each
    extracted = []
    for arr in categories:
        extracted.append(list(arr))
    
    with open('categories.json', 'w') as f:
        json.dump(extracted, f)
    print("Categories saved to categories.json")
else:
    print("No OneHotEncoder found. Might be using another encoding.")
