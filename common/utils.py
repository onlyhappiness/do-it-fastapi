from datetime import datetime

def get_current_timestamp():
    """
    현재 시간을 ISO 형식으로 반환.
    """
    return datetime.now().isoformat()
