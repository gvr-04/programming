package com.example.madapp1;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import android.widget.Toast;


import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private TodoAdapter adapter;
    private EditText editTextTask;
    private Button buttonAdd;
    private RecyclerView recyclerView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editTextTask = findViewById(R.id.editTextTask);
        buttonAdd = findViewById(R.id.buttonAdd);
        recyclerView = findViewById(R.id.recyclerView);

        adapter = new TodoAdapter(this, new ArrayList<>());
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setAdapter(adapter);

        buttonAdd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String taskText = editTextTask.getText().toString().trim();
                if (!TextUtils.isEmpty(taskText)) {
                    adapter.addItem(new TodoItem(taskText));
                    editTextTask.setText("");
                    InputMethodManager imm = (InputMethodManager) getSystemService(INPUT_METHOD_SERVICE);
                    if (imm != null) {
                        imm.hideSoftInputFromWindow(view.getWindowToken(), 0);
                    }
                    Toast.makeText(MainActivity.this, "たすくがついかされました", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
