class ResultResponse:
    """
    用来中转response的，因为返回的数据是response.json()
    没有办法来断言response.status_code,所以封装这个类来保存ResultResponse.success=True
    ResultResponse.body=response.json()
    """
    def __init__(self):
        pass