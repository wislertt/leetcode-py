import warnings

import graphviz


def handle_graphviz_fallback(e: Exception, fallback_content: str) -> str:
    if isinstance(e, graphviz.ExecutableNotFound):
        msg = (
            f"Visual rendering failed: Graphviz not installed ({e!s}). Using text display instead."
        )
    else:
        msg = f"Visual rendering failed: Missing dependencies ({e!s}). Using text display instead."
    warnings.warn(msg, UserWarning)
    return f"<pre>{fallback_content}</pre>"
