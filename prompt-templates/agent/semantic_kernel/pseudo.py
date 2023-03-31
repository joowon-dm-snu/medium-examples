# here's pseudo code for the semantic-kernel's planner
# Planner is not implemented in python-semantic-kernel yet

from typing import ClassVar

from bucket_output import BucketFunctionDefinition
from function_flow import FunctionFlowFunctionDefinition
from problem_solver import (
    ProblemSolverFunctionDefinition,
    SolveNextStepFunctionDefinition,
)

CreateSemanticFunction = ClassVar("CreateSemanticFunction")
FunctionFlowRunner = ClassVar("FunctionFlowRunner")


class Planner:
    def __init__(self) -> None:
        self._functionFlowRunner = FunctionFlowRunner()

        self._bucketFunction = CreateSemanticFunction(
            promptTemplate=BucketFunctionDefinition,
        )

        self._functionFlowFunction = CreateSemanticFunction(
            promptTemplate=FunctionFlowFunctionDefinition,
            description="Given a request or command or goal generate a step by step plan to "
            + "fulfill the request using functions. This ability is also known as decision making and function flow",
            stopSequences="<!--",
        )

        # Currently not exposed -- experimental.
        _ = CreateSemanticFunction(
            ProblemSolverFunctionDefinition,
            description="Given a request or command or goal generate a step by step plan to fulfill the request. "
            + "This ability is also known as decision making and problem solving",
            stopSequences="<!--",
        )

        _ = CreateSemanticFunction(
            SolveNextStepFunctionDefinition,
            description="Given a plan with a goal, take the first step and execute it",
            stopSequences=["<!-- END -->", "<!--"],
        )

    async def create_plan_async(self, **kwargs):
        return await self._functionFlowFunction(**kwargs)

    async def bucket_outputs_async(self, **kwargs):
        return await self._bucketFunction(**kwargs)

    async def execute_plan_async(self, **kwargs):
        return await self._functionFlowRunner(**kwargs)


def main():
    planner = Planner()
    plans = planner.create_plan_async()
    outputs = planner.execute_plan_async(plans)
    response = planner.bucket_outputs_async(outputs)
    return response
