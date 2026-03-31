package com.example.madapp1;

import android.content.Context;
import android.graphics.Paint;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.TextView;
import android.widget.Toast;

import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TodoAdapter extends RecyclerView.Adapter<TodoAdapter.TodoViewHolder> {

    private final List<TodoItem> todoList;
    private final Context context;

    public TodoAdapter(Context context, List<TodoItem> todoList) {
        this.context = context;
        this.todoList = todoList;
    }

    public static class TodoViewHolder extends RecyclerView.ViewHolder {
        CheckBox checkBox;
        TextView textView;

        public TodoViewHolder(View itemView) {
            super(itemView);
            checkBox = itemView.findViewById(R.id.checkBox);
            textView = itemView.findViewById(R.id.textViewTask);
        }
    }

    @Override
    public TodoViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_todo, parent, false);
        return new TodoViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(TodoViewHolder holder, int position) {
        TodoItem item = todoList.get(position);

        // Temporarily remove listener to avoid unwanted triggers
        holder.checkBox.setOnCheckedChangeListener(null);

        holder.textView.setText(item.getTask());
        holder.checkBox.setChecked(item.isDone());

        // Apply or remove strikethrough
        if (item.isDone()) {
            holder.textView.setPaintFlags(holder.textView.getPaintFlags() | Paint.STRIKE_THRU_TEXT_FLAG);
        } else {
            holder.textView.setPaintFlags(holder.textView.getPaintFlags() & (~Paint.STRIKE_THRU_TEXT_FLAG));
        }

        // Re-attach listener
        holder.checkBox.setOnCheckedChangeListener((buttonView, isChecked) -> {
            item.setDone(isChecked);
            sortList(); // Now safe
            if (isChecked) {
                Toast.makeText(context, "よくできました！", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(context, "がんばってね！", Toast.LENGTH_SHORT).show();
            }
//            if (isChecked) {
//                Toast.makeText(context, "Item marked as done: " + item.getTask(), Toast.LENGTH_SHORT).show();
//            } else {
//                Toast.makeText(context, "Item marked as not done: " + item.getTask(), Toast.LENGTH_SHORT).show();
//            }
        });
    }


    @Override
    public int getItemCount() {
        return todoList.size();
    }

    public void addItem(TodoItem item) {
        todoList.add(item);
        sortList();
    }

    private void sortList() {
        Collections.sort(todoList, (a, b) -> {
            if (a.isDone() == b.isDone()) return 0;
            return a.isDone() ? 1 : -1;
        });
        notifyDataSetChanged(); // Rebind everything
    }

}
