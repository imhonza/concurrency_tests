from typing import List, Dict, Any

from plotly.subplots import make_subplots
import plotly.graph_objects as go

def extract_tasks(benchmark_results: List[Dict[str, Any]]) -> List[str]:
    return sorted(
        set(
            task["task"]
            for strategy_result in benchmark_results
            for task in strategy_result["tasks"]
        )
    )

def extract_strategies(benchmark_results: List[Dict[str, Any]]) -> List[str]:
    return [result["strategy"] for result in benchmark_results]

def get_task_times(benchmark_results: List[Dict[str, Any]], task_name: str) -> List[float]:
    task_times = []
    for strategy_result in benchmark_results:
        task_result = next(
            (
                task
                for task in strategy_result["tasks"]
                if task["task"] == task_name
            ),
            None,
        )
        task_times.append(float(task_result["duration"]) if task_result else 0)
    return task_times

def create_figure(tasks: List[str], strategies: List[str], benchmark_results: List[Dict[str, Any]]) -> go.Figure:
    fig = make_subplots(
        rows=len(tasks),
        cols=1,
        shared_xaxes=True,
        shared_yaxes=False,
        subplot_titles=tasks,
    )

    for i, task_name in enumerate(tasks):
        task_times = get_task_times(benchmark_results, task_name)
        fig.add_trace(
            go.Bar(
                x=strategies,
                y=task_times,
                name=task_name,
                hovertext=[
                    f"Task: {task_name}<br>Duration: {duration}s"
                    for duration in task_times
                ],
                hoverinfo="text",
            ),
            row=i + 1,
            col=1,
        )

    fig.update_layout(
        title="Strategy vs Task Execution Time",
        height=300 * len(tasks),
        width=1000,
        showlegend=False,
        barmode="group",
    )

    fig.update_xaxes(showticklabels=True, title_text="Strategy", tickangle=0)
    fig.update_yaxes(title_text="Time (s)", range=[0, 30])

    return fig

def generate_report(benchmark_results: List[Dict[str, Any]], filename: str) -> None:
    tasks = extract_tasks(benchmark_results)
    strategies = extract_strategies(benchmark_results)
    fig = create_figure(tasks, strategies, benchmark_results)
    fig.write_image(f"{filename}.png")