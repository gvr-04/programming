package com.example.madapp1;

public class TodoItem {
    private String task;
    private boolean isDone;

    public TodoItem(String task) {
        this.task = task;
        this.isDone = false;
    }

    public String getTask() {
        return task;
    }

    public boolean isDone() {
        return isDone;
    }

    public void setDone(boolean done) {
        isDone = done;
    }
}
