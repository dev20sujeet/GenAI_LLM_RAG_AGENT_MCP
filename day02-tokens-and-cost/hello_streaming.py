"""Day 2 part 2 (Gemini) — streaming response with TTFT measurement."""
import os
import time
from dotenv import load_dotenv
from google import genai
from rich.console import Console

load_dotenv()
console = Console()


def main() -> None:
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    prompt = "Write a 100-word explanation of what RAG is, in plain English."
    console.print(f"[cyan]Prompt:[/cyan] {prompt}\n")
    console.print("[yellow]Streaming response...[/yellow]\n")

    start = time.perf_counter()
    ttft = None
    chunk_count = 0
    output_tokens = 0

    # generate_content_stream returns an iterator of chunks
    for chunk in client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt,
    ):
        if chunk.text:
            if ttft is None:
                ttft = time.perf_counter() - start
            print(chunk.text, end="", flush=True)
            chunk_count += 1
        # Last chunk carries usage_metadata
        if chunk.usage_metadata:
            output_tokens = chunk.usage_metadata.candidates_token_count or output_tokens

    total_time = time.perf_counter() - start
    print("\n")  # newline after streamed text

    console.print(f"\n[cyan]TTFT (Time To First Token):[/cyan] {ttft:.3f}s")
    console.print(f"[cyan]Total time:[/cyan] {total_time:.3f}s")
    console.print(f"[cyan]Chunks received:[/cyan] {chunk_count}")
    console.print(f"[cyan]Output tokens:[/cyan] {output_tokens}")
    if output_tokens:
        console.print(f"[cyan]Tokens/second:[/cyan] {output_tokens / total_time:.1f}")


if __name__ == "__main__":
    main()