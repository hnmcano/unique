import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import sys
import os
import subprocess

class FlaskService(win32serviceutil.ServiceFramework):
    _svc_name_ = "FlaskTicketServer"
    _svc_display_name_ = "Servidor de Impressão de Tickets"
    _svc_description_ = "Servidor Flask para impressão de tickets"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYSERVICE_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        # Muda para o diretório do script
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Executa o servidor Flask
        subprocess.call([sys.executable, "server.py"])

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(FlaskService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(FlaskService)
