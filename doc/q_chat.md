#  UNDER CONSTRUCTION !
the q_chat script allows you to chat with the Amazon Q assistant from a shell script.
The question prompt is sent to the Q application (defined by its id) and a json structure is returned.

If you don't provide a conversation id, Amazon Q will assume that you start a new conversation with him.

If you provide a conversation id (obtained from a previous exchange in field xyz) the Q assistant will assume that you continue this conversation and restore the context of this precedent conversation to continue the chat.

This script is based on the chat_sync() API provided by the Amazon Q service.

The userid should be one of the user created in the Q application as per documentation