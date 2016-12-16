from zstacklib.utils import httpfrom zstacklib.utils import logfrom zstacklib.utils import threadlogger = log.get_logger(__name__)class ProgressReportCmd(object):    def __init__(self):        self.progress = None        self.processType = None        self.resourceUuid = None        self.serverUuid = Noneclass Progress(object):    def __init__(self):        self.total = 0        self.stage = 1        self.stages = {1: "0:100"}        self.processType = None        self.resourceUuid = None        self.flag = "reports"    def getScale(self):        stages = self.stages.get(self.stage) if self.stages.get(self.stage) else "0:100"        start = int(stages.split(":")[0]) if int(stages.split(":")[0]) > 0 else 0        end = int(stages.split(":")[1]) if int(stages.split(":")[1]) < 100 else 100        assert start < end        return start, end    def getStart(self):        self.stages.keys().sort()        if self.stage == self.stages.keys()[0]:            return "start"        return self.getReport()    def getEnd(self):        self.stages.keys().sort()        if self.stage == self.stages.keys()[-1]:            return "finish"        return self.getReport()    def getReport(self):        return "report"class Report(object):    url = None    serverUuid = None    def __init__(self):        self.resourceUuid = None        self.progress = None        self.header = None        self.processType = None    @thread.AsyncThread    def report(self):        cmd = ProgressReportCmd()        cmd.serverUuid = Report.serverUuid        cmd.processType = self.processType        cmd.progress = self.progress        cmd.resourceUuid = self.resourceUuid        logger.debug("url: %s, cmd: %s, header: %s", Report.url, cmd, self.header)        http.json_dump_post(Report.url, cmd, self.header)