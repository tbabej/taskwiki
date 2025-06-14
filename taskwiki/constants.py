DEFAULT_VIEWPORT_VIRTUAL_TAGS = ("-DELETED", "-PARENT")
DEFAULT_SORT_ORDER = "status+,end+,due+,priority-,project+"

COMPLETION_DATE = """
    now
    yesterday today tomorrow
    later someday

    monday tuesday wednesday thursday friday saturday sunday

    january february march april may june july
    august september october november december

    sopd sod sond eopd eod eond
    sopw sow sonw eopw eow eonw
    sopww soww sonww eopww eoww eonww
    sopm som sonm eopm eom eonm
    sopq soq sonq eopq eoq eonq
    sopy soy sony eopy eoy eony

    goodfriday easter eastermonday ascension pentecost
    midsommar midsommarafton juhannus
""".split()

COMPLETION_RECUR = """
    daily day weekdays weekly biweekly fortnight monthly
    quarterly semiannual annual yearly biannual biyearly
""".split()

# Produced by: $ task _tags | grep -P '[A-Z]+'
VIRTUAL_TAGS = set("""
    ACTIVE
    ANNOTATED
    BLOCKED
    BLOCKING
    CHILD
    COMPLETED
    DELETED
    DUE
    DUETODAY
    INSTANCE
    LATEST
    MONTH
    ORPHAN
    OVERDUE
    PARENT
    PENDING
    PRIORITY
    PROJECT
    QUARTER
    READY
    SCHEDULED
    TAGGED
    TEMPLATE
    TODAY
    TOMORROW
    UDA
    UNBLOCKED
    UNTIL
    WAITING
    WEEK
    YEAR
    YESTERDAY
""".split())
