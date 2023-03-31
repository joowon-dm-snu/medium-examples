BucketFunctionDefinition = """1. Given an output of a function, bucket the output into a list of results.

Examples:
[CONTENT]
Result 1
This is the first result.
Result 2
This is the second result. It's doubled!
Result 3
This is the third and final result. Truly astonishing.
[END CONTENT]

EXPECTED BUCKETS:

Result:
{""buckets"": [""Result 1
This is the first result."", ""Result 2
This is the second result. It's doubled!"", ""Result 3
This is the third and final result. Truly astonishing.""]}

End examples.

[CONTENT]
{{$input}}
[END CONTENT]

EXPECTED BUCKETS: {{$bucketCount}}

Result:
"""
