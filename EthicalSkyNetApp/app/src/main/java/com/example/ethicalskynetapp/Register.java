package com.example.ethicalskynetapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class Register extends AppCompatActivity implements View.OnClickListener {

    Button register;
    EditText fname,lName,phone, password,email, address;
    TextView back;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);


        email = (EditText) findViewById(R.id.Email);
        password = (EditText) findViewById(R.id.Password);
        phone = (EditText) findViewById(R.id.Phone);
        fname = (EditText) findViewById(R.id.FName);
        lName = (EditText)findViewById(R.id.LName);
        address = (EditText) findViewById(R.id.Address);
        register = (Button)findViewById(R.id.Register);
        back = (TextView)findViewById(R.id.Back);

        register.setOnClickListener(this);
        back.setOnClickListener(this);

    }

    @Override
    public void onClick(View v) {
        switch (v.getId())
        {
            case R.id.Register:
                break;

            case R.id.Back:
                startActivity(new Intent(this, MainActivity.class));
                break;
        }
    }
}
