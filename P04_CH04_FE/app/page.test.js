import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import Home from './page.tsx';


test('renders learn react link', () => {
    render(<Home />);
    const linkElement = screen.getByText(/Get started by editing/i);
    expect(linkElement).toBeInTheDocument();
});