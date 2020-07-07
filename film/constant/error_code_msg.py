
class ErrorCodeMsg:
    PARAMERR = "300001"
    NOSTUDYERR = "300002"
    TASKTYPEERR = "300003"
    NORESULTERR = "300004"
    SERVERERR = "3000nn-1"
    UNKNOWERR = "3000nn"


error_dict = {
    ErrorCodeMsg.PARAMERR: "Miss params",
    ErrorCodeMsg.NOSTUDYERR: "Not find study info",
    ErrorCodeMsg.TASKTYPEERR: "Not find task type",
    ErrorCodeMsg.NORESULTERR: "Not find result",
    ErrorCodeMsg.UNKNOWERR: "Unknown error",
}
