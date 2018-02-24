function [J, grad] = lrCostFunction(theta, X, y, lambda)
%LRCOSTFUNCTION Compute cost and gradient for logistic regression with 
%regularization
%   J = LRCOSTFUNCTION(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Hint: The computation of the cost function and gradients can be
%       efficiently vectorized. For example, consider the computation
%
%           sigmoid(X * theta)
%
%       Each row of the resulting matrix will contain the value of the
%       prediction for that example. You can make use of this to vectorize
%       the cost function and gradient computations. 
%
% Hint: When computing the gradient of the regularized cost function, 
%       there're many possible vectorized solutions, but one solution
%       looks like:
%           grad = (unregularized gradient for logistic regression)
%           temp = theta; 
%           temp(1) = 0;   % because we don't add anything for j = 0  
%           grad = grad + YOUR_CODE_HERE (using the temp variable)
%
function [J, grad] = costFunctionReg(theta, X, y, lambda)
J = 0;
grad = zeros(size(theta));

temp_theta = [];

for jj = 2:length(theta)

    temp_theta(jj) = theta(jj)^2;
end

theta_reg = lambda/(2*m)*sum(temp_theta);

temp_sum =[];

for ii =1:m

   temp_sum(ii) = -y(ii)*log(sigmoid(theta'*X(ii,:)'))-(1-y(ii))*log(1-sigmoid(theta'*X(ii,:)'));

end

tempo = sum(temp_sum);

J = (1/m)*tempo+theta_reg;

%regulatization
%theta 0

reg_theta0 = 0;

for i=1:m
    reg_theta0(i) = ((sigmoid(theta'*X(i,:)'))-y(i))*X(i,1)
end

theta_temp(1) = (1/m)*sum(reg_theta0)

grad(1) = theta_temp

sum_thetas = []
thetas_sum = []

for j = 2:size(theta)
    for i = 1:m

        sum_thetas(i) = ((sigmoid(theta'*X(i,:)'))-y(i))*X(i,j)
    end

    thetas_sum(j) = (1/m)*sum(sum_thetas)+((lambda/m)*theta(j))
    sum_thetas = []
end

for z=2:size(theta)
    grad(z) = thetas_sum(z)
end


% =============================================================

end









% =============================================================

grad = grad(:);

end
