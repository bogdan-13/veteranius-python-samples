# implement your own retry decorator

# should retry function execution in case of an error
@retry # just retry 3 times, 1 sec wait

@retry(
    times=4, # should retry this number of times - 1 (defaults to 3)
    include=[ValueError, FileNotFoundError], # should retry only errors from this list, 
                                             # by default retries all exceptions
    exclude=[FileNotFoundError], # these errors should be excluded from retrying
                                 # exclude overrides include or defaults
    backoff=backoff( # policy of waiting between reties
        delay=1000, # min wait time betqween retries in milliseconds
        maxDelay=1000, # max wait time
        random=False # if wait time between min and max should be randomized
    )
)

# waits between attempts: 500, 1000, 1500
@retry(
    backoff=backoff(
        delay=500,
        maxDelay=1500
    )
)

# 3 attempts each wait time randomized between 500 and 1500
@retry(
    backoff=backoff(
        delay=500,
        maxDelay=1500,
        random=True
    )
)