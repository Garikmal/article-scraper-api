from fastapi.responses import JSONResponse

def http_error_response(status_code: int, detail: str):
    return JSONResponse(
        status_code=status_code,
        content={"error": detail}
    )
