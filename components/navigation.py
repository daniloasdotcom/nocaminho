from routes.studies import studies

def get_prev_next(current_path):
    paths = [s["path"] for s in studies]
    idx = paths.index(current_path)
    prev_study = studies[idx - 1] if idx > 0 else None
    next_study = studies[idx + 1] if idx < len(studies) - 1 else None
    return prev_study, next_study