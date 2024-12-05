from fastapi import Request
from fastapi.responses import JSONResponse, Response
from datetime import datetime

# 현재 시간 반환 함수
def get_current_timestamp():
    return datetime.now().isoformat()

# Custom Middleware
async def custom_response_middleware(request: Request, call_next):
    try:
        # 원본 응답 처리
        response = await call_next(request)

        # StreamingResponse나 FileResponse는 그대로 반환
        if isinstance(response, Response) and not isinstance(response, JSONResponse):
            return response

        # JSON 형태의 응답 데이터 처리
        if hasattr(response, "body_iterator"):
            original_body = b"".join([chunk async for chunk in response.body_iterator])
            response = JSONResponse(
                content={
                    "success": True,
                    "data": original_body.decode("utf-8") if original_body else None,
                    "timestamp": get_current_timestamp(),
                },
                status_code=response.status_code,
            )
        return response

    except Exception as e:
        # 에러가 발생한 경우 기본 실패 응답 반환
        return JSONResponse(
            content={
                "success": False,
                "data": str(e),
                "timestamp": get_current_timestamp(),
            },
            status_code=500,
        )
