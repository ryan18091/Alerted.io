from datetime import datetime

def SnowFallStandardMSG(SMSVars):
    print(SMSVars)
    Zipcode = SMSVars[5]
    AlertTime = SMSVars[2]
    TotalSnowFall = SMSVars[4]
    StartTime = SMSVars[3]
    StartTime = (StartTime.strftime("%I:%M %p"))

    body = """" -You've been ALERTED-\n Snowfall for %r between %r and %r has been recorded at %s in.""" %(Zipcode,
                                                                           StartTime, AlertTime, TotalSnowFall)
    return body

def CustomMSG(SMSVars):
    pass