import numpy as np
from query_search import search_books

def normalize(text):
    """Lowercase and strip text for comparison."""
    return text.strip().lower()

def precision_at_k(relevant, retrieved, k):
    retrieved_k = retrieved[:k]
    if not retrieved_k:
        return 0.0
    relevant_retrieved = [doc for doc in retrieved_k if doc in relevant]
    return len(relevant_retrieved) / len(retrieved_k)

def recall_at_k(relevant, retrieved, k):
    retrieved_k = retrieved[:k]
    if not relevant:
        return 0.0
    relevant_retrieved = [doc for doc in retrieved_k if doc in relevant]
    return len(relevant_retrieved) / len(relevant)

def reciprocal_rank(relevant, retrieved):
    for idx, doc in enumerate(retrieved, start=1):
        if doc in relevant:
            return 1.0 / idx
    return 0.0

def ndcg_at_k(relevant, retrieved, k):
    dcg = 0.0
    for i, doc in enumerate(retrieved[:k]):
        rel = 1.0 if doc in relevant else 0.0
        dcg += (2**rel - 1) / np.log2(i + 2)

    ideal_rels = [1.0] * min(len(relevant), k)
    idcg = sum((2**rel - 1) / np.log2(i + 2) for i, rel in enumerate(ideal_rels))
    if idcg == 0:
        return 0.0
    return dcg / idcg

def evaluate_query(query, relevant_titles, k=10):
    results = search_books(query, size=k)
    retrieved_titles = [normalize(doc.get("Title", "")) for doc in results]

    relevant_titles = [normalize(t) for t in relevant_titles]
    
    prec = precision_at_k(relevant_titles, retrieved_titles, k)
    rec = recall_at_k(relevant_titles, retrieved_titles, k)
    rr = reciprocal_rank(relevant_titles, retrieved_titles)
    ndcg = ndcg_at_k(relevant_titles, retrieved_titles, k)
    
    return prec, rec, rr, ndcg, results

def main():
    sample_queries = {
        "flu pandemic 1918": ["The Great Influenza"],
        "kitchen gods": ["The Kitchen God's Wife"],
        "pirates": ["Pirates!"],
        "pride and prejudice": ["Pride and Prejudice"],
        "beloved": ["Beloved"]
    }

    k = 20
    all_prec, all_rec, all_rr, all_ndcg = [], [], [], []

    print("Evaluation Results:\n" + "-" * 40)
    for query, relevant_titles in sample_queries.items():
        prec, rec, rr, ndcg, retrieved = evaluate_query(query, relevant_titles, k)
        
        print(f"\nQuery: '{query}'")
        print(f"Expected Relevant Titles: {[normalize(t) for t in relevant_titles]}")
        print(f"Top-{k} Retrieved Titles:")
        for i, book in enumerate(retrieved[:k], 1):
            print(f"{i}. {book.get('Title', 'N/A')} (ISBN: {book.get('ISBN', 'N/A')})")

        print(f"\nPrecision@{k}: {prec:.2f}")
        print(f"Recall@{k}: {rec:.2f}")
        print(f"Reciprocal Rank: {rr:.2f}")
        print(f"NDCG@{k}: {ndcg:.2f}")
        
        all_prec.append(prec)
        all_rec.append(rec)
        all_rr.append(rr)
        all_ndcg.append(ndcg)

    print("\nOverall Evaluation Metrics:")
    print(f"Mean Precision@{k}: {np.mean(all_prec):.2f}")
    print(f"Mean Recall@{k}: {np.mean(all_rec):.2f}")
    print(f"Mean Reciprocal Rank (MRR): {np.mean(all_rr):.2f}")
    print(f"Mean NDCG@{k}: {np.mean(all_ndcg):.2f}")

if __name__ == "__main__":
    main()
