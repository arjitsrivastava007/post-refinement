import streamlit as st
from graph.workflow import app


def main():
    # Streamlit frontend
    st.title("Post Critique and Improvement App")

    # User input
    post_content = st.text_area("Enter your post content below:", height=200)

    if st.button("Submit"):
        # Initialize state
        state = {
            "post": post_content,
            "critique": "",
            "iteration": 0,
            "history": []
        }

        # Run the workflow
        for _ in range(3):
            state = app.invoke(state)

        # Display final results
        st.subheader("Final Post Content")
        st.write(state["post"])

        st.subheader("Critique and Improvement History")
        for step in state["history"]:
            st.write(f"Iteration {step['iteration']}:")
            st.write(f"**Critique:** {step['critique']}")
            st.write(f"**Post:** {step['post']}")
            st.write("---")


if __name__ == "__main__":
    main()
