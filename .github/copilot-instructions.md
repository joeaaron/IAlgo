# IAlgo - AI Coding Agent Instructions

## Project Overview
**IAlgo** is an algorithm learning repository demonstrating classic algorithmic problem solutions with an educational focus. The codebase emphasizes **divide-and-conquer** and **recursive problem-solving** patterns.

Current scope: Tower of Hanoi solution with detailed step-by-step recursion.

## Architecture & Key Patterns

### Code Organization
- **Single entry file**: `hannuota.py` - Implements Tower of Hanoi problem
- **Planned module structure**: `Greedy/` folder exists for future greedy algorithm implementations
- **Pattern**: Each algorithm lives in its dedicated module/file

### Algorithmic Approach: Divide-and-Conquer Recursion
The Tower of Hanoi implementation exemplifies the project's teaching approach:
1. **Helper functions**: `move()` performs atomic operations (single disk transfer)
2. **Recursive solver**: `dfs()` breaks problems into `i-1` subproblems with a base case
3. **Public API**: `solve_hanota()` provides the clean entry point

**Code example** (`hannuota.py`):
```python
def dfs(i: int, src: list[int], buf: list[int], tar: list[int]):
    if i == 1:  # Base case
        move(src, tar)
        return
    dfs(i - 1, src, tar, buf)  # Subproblem 1
    move(src, tar)             # Core operation
    dfs(i - 1, buf, src, tar)  # Subproblem 2
```

## Code Style & Conventions

### Type Hints & Documentation
- Use **modern Python type hints**: `list[int]` (not `List[int]`)
- Include docstrings for functions using triple-quoted format:
  ```python
  def function_name(param: type) -> None:
      """Brief description of what the function does"""
  ```

### Variable Naming
- **src/buf/tar**: Standard abbreviations for source/buffer/target stacks (Tower of Hanoi convention)
- **i**: Recursive depth parameter (problem size)
- Chinese comments are used; preserve them for educational clarity

### Problem-Solving Pattern
- Small utility functions for atomic operations
- Separate recursive/complex logic function
- Public-facing wrapper function with clear semantics
- List mutation (`.pop()`, `.append()`) for stack simulation

## When Adding New Algorithms

1. **Create module structure**: Add files to `Greedy/` or new category folders
2. **Follow recursive pattern**: Break into base case + subproblems
3. **Use descriptive names**: Function names should indicate algorithm type (e.g., `solve_*`, `dfs_*`, `greedy_*`)
4. **Atomic operations**: Extract single-step logic into helper functions
5. **Type hints**: Maintain complete type annotations
6. **Documentation**: Include docstrings explaining the divide-and-conquer strategy

## No External Dependencies
This is a pure Python educational project with no external packages. All solutions use only built-in Python data structures (lists for stacks, recursion for logic flow).

## Testing Considerations
The code demonstrates correctness through stack simulation. Verify algorithms with:
- Small input cases (n=1,2,3 for Tower of Hanoi)
- Visual stack state inspection before/after operations
- Recursive call depth tracking for complexity analysis
