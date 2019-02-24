package com.example.ethicalskynetapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class Login extends AppCompatActivity implements View.OnClickListener {

    Button Login;
    EditText email, password;
    TextView back;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        email = (EditText)findViewById(R.id.Email);
        password = (EditText)findViewById(R.id.Password);
        Login = (Button) findViewById(R.id.Login);
        back = (TextView) findViewById(R.id.Back);

        Login.setOnClickListener(this);
        back.setOnClickListener(this);
    }

    @Override
    public void onClick(View v)
    {
        switch (v.getId())
        {
            case R.id.Login:


                break;

            case R.id.Back:
                startActivity(new Intent(this,MainActivity.class));
                break;
        }

    }
}
