from importlib import import_module
from inspect import iscoroutine

from fastapi import FastAPI, HTTPException


app = FastAPI(title="NIFTY F&O Agent")


@app.get("/health")
def health():
    return {"status": "ok"}


def _find_strategy_function():
    """
    Look for the strategy brain in common beginner-friendly file/function names.

    If your project uses a different name, add it to this list.
    """
    candidates = [
        ("strategy_brain", "run"),
        ("strategy_brain", "daily_plan"),
        ("strategy_brain", "run_daily_plan"),
        ("main", "run"),
        ("main", "daily_plan"),
        ("agent", "run"),
        ("agent", "daily_plan"),
        ("nifty_fno_agent", "run"),
        ("nifty_fno_agent", "daily_plan"),
    ]

    for module_name, function_name in candidates:
        try:
            module = import_module(module_name)
        except ModuleNotFoundError:
            continue

        strategy_function = getattr(module, function_name, None)
        if callable(strategy_function):
            return strategy_function

    return None


@app.get("/daily-plan")
async def daily_plan():
    strategy_function = _find_strategy_function()

    if strategy_function is None:
        raise HTTPException(
            status_code=500,
            detail=(
                "Strategy brain not found. Create a function like "
                "strategy_brain.py -> run() that returns the final JSON result."
            ),
        )

    try:
        result = strategy_function()
        if iscoroutine(result):
            result = await result
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
